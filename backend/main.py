#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from pathlib import Path
from typing import Literal

from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

# 获取项目根目录
# 根目录 绝对路径
BasePath = Path(__file__).resolve().parent.parent

# env 环境变量文件
ENV_DIR = os.path.join(BasePath, 'env')


class Settings(BaseSettings):
    ENVIRONMENT: Literal['production', 'development', 'test'] = 'development'

    model_config = SettingsConfigDict(
        env_file=os.path.join(ENV_DIR, f'.env.{os.getenv("ENVIRONMENT", "development")}'),
        env_file_encoding='utf-8',
    )


settings = Settings()
app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': settings.ENVIRONMENT}
