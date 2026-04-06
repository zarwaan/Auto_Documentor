pipeline {
    agent any

    environment {
        GROQ_API_KEY = credentials('groq-api-key')
        GITHUB_CREDS = credentials('github-creds')
    }

    stages {
        stage('Skip CI Check') {
            steps {
                script {
                    def msg = sh(script: "git log -1 --pretty=%B", returnStdout: true).trim()
                    if (msg.contains('[skip ci]')) {
                        echo "Skipping build due to [skip ci]"
                        currentBuild.result = 'NOT_BUILT'
                        error("Stopping pipeline")
                    }
                }
            }
}

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install groq
                '''
            }
        }

        stage('Generate Documentation') {
            steps {
                sh '''
                . venv/bin/activate
                python generate_docs.py
                '''
            }
        }

        stage('Commit and Push README') {
            steps {
                sh '''
                git config user.name "zarwaan"
                git config user.email "zarwaanshroff@gmail.com"

                git add README.md
                git diff-index --quiet HEAD || git commit -m "docs: Auto-update README by AI [skip ci]"

                git push https://${GITHUB_CREDS_USR}:${GITHUB_CREDS_PSW}@github.com/zarwaan/Auto_Documentor.git HEAD:main
                '''
            }
        }
    }
}