def test_simple_dataset_manifest_samples():
    from src.data.loader import SimpleDataset
    # uses sample manifest created earlier at data/manifest_samples.json
    ds = SimpleDataset('data/manifest_samples.json', root='.')
    assert len(ds) == 3
    item = ds[0]
    assert 'image' in item
    assert 'meta' in item
    assert item['meta']['index'] == 0
