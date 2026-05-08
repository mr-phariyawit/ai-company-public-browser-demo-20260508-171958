from core_service.liveness import system_reports_alive


def test_system_reports_alive() -> None:
    assert system_reports_alive() == {"alive": True}
