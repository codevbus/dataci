pipeline {
    agent { docker { image 'amancevice/pandas' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
