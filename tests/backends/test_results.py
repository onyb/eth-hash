import pytest

# Note that this file is symlink'd in all backend folders, so a change here is
# automatically shared across backend tests. If you want to add a backend-specific
# test, add it to a new file.


@pytest.fixture
def keccak_auto():
    from eth_hash.auto import keccak
    return keccak


@pytest.mark.parametrize(
    'prehash, expected_result',
    (
        (
            b'',
            b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';{\xfa\xd8\x04]\x85\xa4p",  # noqa: E501
        ),
    ),
)
def test_keccak_256(keccak, prehash, expected_result):
    assert keccak(prehash) == expected_result
