# MyTFlib - TensorFlow 기반 Computer Vision 개발 환경

이 프로젝트는 GitHub Codespaces와 Docker를 기반으로 Python 3.9 + TensorFlow 2.8.4 GPU 환경을 구축하고,  
Custom 라이브러리 및 ONNX 변환, Cython 모듈 빌드까지 포함한 실전 개발용 환경을 제공합니다.

---

## ✅ 주요 기능 및 구성

- Python 3.9 + TensorFlow 2.8.4 (GPU)
- Computer Vision 관련 주요 패키지 포함
- `src/myTFlib` 커스텀 모듈 구조
- `.env`를 통한 민감 정보 관리
- `pytest` 기반 테스트
- `Cython` 모듈 작성 및 컴파일 예제 포함
- `setup.py` + `MANIFEST.in` + `build`로 패키징 가능
- Linter / Formatter (`flake8`, `black`) 자동 적용
- Codespaces에서 Docker 기반 devcontainer 자동 실행

---

## 1. 개발 시작 (GitHub Codespaces)

1. 이 저장소를 Fork 또는 Clone
2. GitHub 웹에서 `Code > Codespaces > Create codespace` 클릭
3. `.devcontainer/` 설정을 바탕으로 Docker 이미지가 자동 빌드되고, 패키지 설치됨

---

## 2. 환경 구성 구조

```bash
requirements.txt           # 런타임 패키지
dev-requirements.txt       # 개발 도구 (pytest, black, flake8, etc)
setup.py                   # 패키징 및 의존성 관리
MANIFEST.in                # 패키징 파일 포함 설정
src/myTFlib/               # 커스텀 라이브러리
tests/                     # pytest 테스트 모듈
```

---

## 3. `.env` 파일 사용

```env
DEBUG=True
API_KEY=test-key-1234
```

사용 예시:

```python
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")
```

> `.env`는 `.gitignore`에 포함되어 Git에는 업로드되지 않습니다.

---

## 4. 테스트 실행

```bash
pytest
```

- `tests/` 폴더 내 `test_*.py` 파일 자동 인식
- 테스트 함수 이름은 반드시 `test_`로 시작해야 합니다.

---

## 5. Cython 모듈 작성 및 컴파일

### 예시 파일: `src/myTFlib/cython_module.pyx`

```cython
def multiply(int a, int b):
    return a * b
```

### 컴파일 방법

```bash
pip install cython
python setup.py build_ext --inplace
```

> 컴파일 결과:  
> - Linux: `.so` 파일  
> - Windows: `.pyd` 파일

### 사용 방법

```python
from myTFlib.cython_module import multiply
print(multiply(3, 4))  # 결과: 12
```

---

## 6. 코드 린트 & 포맷

### 커맨드 실행

```bash
flake8 src/
black src/
```

### VSCode 자동 설정 (.devcontainer.json 내부 포함)
- 저장 시 `black` 자동 포맷
- `flake8` 실시간 코드 검사

---

## 7. 패키징 (whl 파일 만들기)

```bash
pip install build
python -m build
```

> `dist/` 폴더에 `.whl`, `.tar.gz` 파일이 생성됨

---

## 8. 커스텀 라이브러리 설치

Codespaces나 로컬에서 다음과 같이 개발 모드로 설치:

```bash
pip install -e .[dev]
```

---

## 📁 디렉토리 구조 예시

```
your-project/
├── .env
├── .gitignore
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── requirements.txt
├── dev-requirements.txt
├── setup.py
├── MANIFEST.in
├── README.md
├── src/
│   └── myTFlib/
│       ├── __init__.py
│       ├── example.py
│       └── cython_module.pyx
└── tests/
    └── test_example.py
```