from app.expert_system import build_demo_system


def test_no_image_rule():
    system = build_demo_system()
    diagnosis = system.diagnose({
        "power_on": True,
        "no_image": True,
        "monitor_on": True,
    })

    assert "video_cable" in diagnosis["diagnostic_steps"]


def test_power_rule():
    system = build_demo_system()
    diagnosis = system.diagnose({
        "power_on": False,
    })

    assert "power_supply" in diagnosis["diagnostic_steps"]
