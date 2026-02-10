pipeline {
    agent any

    tools {
        allure 'allure'   // name configured in Jenkins Tools
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests - Chrome') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest tests --browser=chrome --alluredir=reports\\allure-results
                '''
            }
        }

        stage('Run Tests - Edge') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest tests --browser=edge --alluredir=reports\\allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Test execution completed'
        }
        success {
            echo 'Build Passed'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
