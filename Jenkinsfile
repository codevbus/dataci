pipeline {
    agent none
    stages {
        stage('validate') {
            agent {
                docker { image 'amancevice/pandas' }
            }
            steps {
                sh 'python validate.py healthcare-dataset-stroke-data.csv'
            }
        }
        stage('cleanup') {
            agent {
                docker { image 'amancevice/pandas' }
            }
            steps {
                sh 'python cleanup.py'
            }
        }
        stage('deploy') {
            agent {
                docker { image 'amancevice/pandas' }
            }
            steps {
                sh 'python validate.py clean.csv'
            }
        }
        stage('vizualize') {
            agent {
                docker { image 'czentye/matplotlib-minimal' }
            }
            steps {
                sh 'python vizualize.py'
            }
        }
    }
}
