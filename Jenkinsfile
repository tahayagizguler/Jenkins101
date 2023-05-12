pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '*/5 * * * *'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building..."
                    sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo "Testing..."
                    sh 'python checkStatus.py'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying..."
            }
        }
    }
}
