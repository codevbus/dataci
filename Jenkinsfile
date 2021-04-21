pipeline {
    agent none
    stages {
        stage('validate') {
            agent {
                docker { image 'amancevice/pandas' }
            }
            steps {
                sh 'python validate.py healthcare-dataset-stroke-data.csv'
                sh 'docker stop amancevice/pandas'
            }
        }
        stage('cleanup') {
            agent {
                docker { image 'amancevice/pandas' }
            }
            steps {
                sh 'python cleanup.py'
                stash includes: '*clean*', name: 'csv'
                sh 'docker stop amancevice/pandas'
            }
        }
        stage('deploy') {
            agent {
                docker { image 'amancevice/pandas' }
            }
            steps {
                unstash name: 'csv'
                sh 'python validate.py clean.csv'
                sh 'docker stop amancevice/pandas'
            }
        }
        stage('vizualize') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                sh 'python vizualize.py'
            }
        }
    }
}
