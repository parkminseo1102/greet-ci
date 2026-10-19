# greet-ci

인사말 프로그램 및 GitHub Actions CI 워크플로우 실습 프로젝트입니다.

## 실행 방법

### 기본 실행
```bash
uv run --locked python greet.py
```
출력:
```text
Hello, world!
```

### 이름 인수를 지정한 실행
```bash
uv run --locked python greet.py Hee
```
출력:
```text
Hello, Hee!
```

## 테스트 및 품질 검사

```bash
uv run --locked pytest -q greet.py
uv run --locked black --check greet.py
uv run --locked flake8 greet.py
uv run --locked mypy greet.py
```

## 패키지 빌드

```bash
uv build
```