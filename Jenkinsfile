pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    environment {
        GROQ_API_KEY = credentials('groq-api-key')
        GITHUB_CREDS = credentials('github-creds')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/zarwaan/Auto_Documentor.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install groq'
            }
        }

        stage('Generate Documentation') {
            steps {
                sh 'python generate_docs.py'
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