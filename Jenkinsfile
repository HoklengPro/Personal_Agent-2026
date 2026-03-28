pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 --max-line-length=120 --exclude=venv,migrations .
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py test --verbosity=2
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop django-app || true
                    docker rm django-app || true
                    docker run -d --name django-app -p 8000:8000 django-app:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
