pipeline {
    agent any
    environment {
        GIT_TAG = sh(returnStdout: true,script: 'git describe --tags').trim()
        REGISTRY_HOST = "tezign.com:5000"
        DOCKER_IMAGE = "prometheus_client_metrics"
        APP_NAME = "prometheus_client_metrics"
    }
    parameters {
        //string(name: 'K8S_NAMESPACE', defaultValue: 'env6', description: 'k8s的namespace名称')
        choice(name:'K8S_NAMESPACE',choices:'env5\nenv6',description:'k8s的namespace名称')
    }
    stages {
        stage('image') {
            steps {
                sh "docker build -t ${params.REGISTRY_HOST}/${params.DOCKER_IMAGE}:${GIT_TAG} ."
                sh "docker push ${params.REGISTRY_HOST}/${params.DOCKER_IMAGE}:${GIT_TAG} "
            }
        }
    }
}