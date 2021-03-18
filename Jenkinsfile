pipeline {
    agent { docker { image 'amancevice/pandas' } }
    stages {
        stage('validate') {
            steps {
                sh 'python validate.py'
            }
        stage('test') {
            steps {
                sh 'python --version'
            }
        stage('deploy') {
            steps {
                sh 'python --version'
            }
        }
    }
}
