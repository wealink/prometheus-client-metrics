pipeline {
    agent any
    parameters {
        string(name: 'REGISTRY_HOST', defaultValue: 'tezign.com:5000', description: '仓库地址')
        string(name: 'DOCKER_IMAGE', defaultValue: 'prometheus_client_metrics', description: 'docker镜像名')
        string(name: 'APP_NAME', defaultValue: 'prometheus_client_metrics', description: 'k8s中标签名')
        string(name: 'K8S_NAMESPACE', defaultValue: 'env6', description: 'k8s的namespace名称')
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