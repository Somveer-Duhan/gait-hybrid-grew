def test_visibility_and_enhancer():
    from src.preprocessing.visibility_filter import VisibilityFilter
    from src.preprocessing.selective_enhancer import SelectiveEnhancer
    vf = VisibilityFilter(min_bbox_area=100)
    assert vf.keep(150, 0.5)
    se = SelectiveEnhancer()
    from PIL import Image
    img = Image.new('RGB',(64,128),(120,120,120))
    out = se.enhance(img)
    assert out is not None
