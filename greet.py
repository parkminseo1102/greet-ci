import sys


def greet(name: str = "world") -> str:
    """주어진 이름으로 인사말 문자열을 반환합니다."""
    return f"Hello, {name}!"


def main() -> None:
    """실행 진입점: 명령행 인수를 읽어 인사말을 표준 출력으로 한 줄 출력합니다."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))


def test_greet() -> None:
    """pytest 및 테스트 실행을 위한 단언문입니다."""
    assert greet("Hee") == "Hello, Hee!"
    assert greet("world") == "Hello, world!"


if __name__ == "__main__":
    main()
