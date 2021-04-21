pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '--entrypoint='
        }
    }
    stages {
        stage('validate') {
            steps {
                sh 'python validate.py healthcare-dataset-stroke-data.csv'
            }
        }
        stage('cleanup') {
            steps {
                sh 'python cleanup.py'
                stash includes: '*clean*', name: 'csv'
            }
        }
        stage('deploy') {
            steps {
                unstash name: 'csv'
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
