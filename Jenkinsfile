pipeline {
    agent { docker { image 'amancevice/pandas' } }
    stages {
        stage('validate') {
            steps {
                sh 'python validate.py healthcare-dataset-stroke-data.csv'
            }
        }
        stage('cleanup') {
            steps {
                sh 'python cleanup.py'
            }
        }
        stage('deploy') {
            steps {
                sh 'python validate.py clean.csv'
            }
        }
        stage('vizualize') {
            steps {
                sh 'python vizualize.py'
            }
        }
    }
}
