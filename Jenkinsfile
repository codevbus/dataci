pipeline {
    agent none
    stages {
        stage('validate') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                sh 'python validate.py healthcare-dataset-stroke-data.csv'
            }
        }
        stage('cleanup') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                sh 'python cleanup.py'
                stash includes: '*clean*', name: 'csv'
            }
        }
        stage('deploy') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                unstash name: 'csv'
                sh 'python validate.py clean.csv'
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
