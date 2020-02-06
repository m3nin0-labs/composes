#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Os testes feitos abaixo foram feitos utilizando as seguintes versões:
#   python-client 10.0.1
#   kubernetes 1.15.0
# Caso tenha dúvidas com a versão da API, consulte a documentação
# https://github.com/kubernetes-client/python

import yaml
from kubernetes import client, config


def load_yaml(yaml_file: str) -> dict:
    """Função para a leitura de arquivos yaml
    
    Args:
        yaml_file (str): Caminho absoluto para o arquivo yaml
    Returns:
        dict: Dicionário com as informações carregadas do arquivo    
    """
    with open(yaml_file) as file:
        return yaml.safe_load(file)

# Carregando as configurações do Kubernetes
# Pode ser necessário utilizar: sudo chmod 606 $HOME/.kube/config (Caso as configurações
# apresentem erros ao serem carregadas)
config.load_kube_config()
v1 = client.CoreV1Api()
beta_api = client.ExtensionsV1beta1Api()

deployment_config = load_yaml("postgis.deploy.yaml")
service_config = load_yaml("postgis.service.yaml")

# Criando os objetos no kubernetes (extensions api)
# o retorno dos métodos de criação é um dict com várias informações úteis
beta_api.create_namespaced_deployment(
     body = deployment_config, namespace = 'default'
)

# core api
v1.create_namespaced_service(
     body = service_config, namespace = 'default'
)
