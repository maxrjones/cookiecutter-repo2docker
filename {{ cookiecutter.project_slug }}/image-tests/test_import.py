# Begin tests, which are useful for ensuring packages are properly installed.

def test_import():
    import platform
    print(platform.python_version())
