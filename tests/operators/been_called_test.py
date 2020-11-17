import pytest
import os
from grappa.operators.been_called import BeenCalledOperator


def test_been_called(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called


    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called


    mock_called_several_times = mocker.patch('os.rename')
    os.rename('/home/log.txt', '/home/log_new.txt')
    os.rename('/home/log.txt', '/home/log_new.txt')

    expect(mock_called_several_times).to.have.been_called

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have_not.been_called


def test_been_called_times(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')
    os.remove('/home/log.txt')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_times(3)

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_times(3)


    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have.been_called_times(0)
    expect(mock_not_called).to.have_not.been_called_times(3)

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_times(3)


def test_been_called_with(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_with('/home/log.txt')


    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_with('/home/log.txt')


def test_been_called_once(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_once


    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_once


    mock_called_several_times = mocker.patch('os.rename')
    os.rename('/home/log.txt', '/home/log_new.txt')
    os.rename('/home/log.txt', '/home/log_new.txt')

    expect(mock_called_several_times).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have.been_called_once


def test_been_called_once_with(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_once_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_once_with('/home/log.txt')


    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_once_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_once_with('/home/log.txt')


    mock_called_several_times = mocker.patch('os.rename')
    os.rename('/home/log.txt', '/home/log_new.txt')
    os.rename('/home/log.txt', '/home/log_new.txt')

    expect(mock_called_several_times).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have.been_called_once