import pytest
import base64
from src.core.util.png_to_base64_util import png_to_base64

def test_png_to_base64_success(tmp_path):
    img_file = tmp_path / "test.png"
    dummy_bytes = b"fake png content"
    img_file.write_bytes(dummy_bytes)
    
    encoded = png_to_base64(str(img_file))
    expected = base64.b64encode(dummy_bytes).decode("utf-8")
    assert encoded == expected

def test_png_to_base64_file_not_found():
    with pytest.raises(FileNotFoundError) as exc_info:
        png_to_base64("non_existent_file.png")
    assert "File not found" in str(exc_info.value)

def test_png_to_base64_invalid_extension(tmp_path):
    txt_file = tmp_path / "test.txt"
    txt_file.write_bytes(b"some text")
    
    with pytest.raises(ValueError) as exc_info:
        png_to_base64(str(txt_file))
    assert "The file must be a PNG image" in str(exc_info.value)
