pipeline {
    agent { docker { image 'python:3.9.2' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}