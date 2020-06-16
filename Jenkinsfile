pipeline {
    agent any
    environment {
        REGISTRY_HOST = "tezign.com:5000"
        DOCKER_IMAGE = "prometheus_client_metrics"
        APP_NAME = "prometheus_client_metrics"
    }
    parameters {
        choice(name:'K8S_NAMESPACE',choices:'env5\n env6',description:'k8s的namespace名称')
        string(name: 'GIT_TAG', defaultValue: '', description: 'GIT_TAG名称')
    }
    stages {
        stage('image') {
            steps {
                sh "docker build -t ${REGISTRY_HOST}/${DOCKER_IMAGE}:${params.GIT_TAG}_${BUILD_ID} ."
                sh "docker push ${REGISTRY_HOST}/${DOCKER_IMAGE}:${params.GIT_TAG}_${BUILD_ID}"
            }
        }
    }
}