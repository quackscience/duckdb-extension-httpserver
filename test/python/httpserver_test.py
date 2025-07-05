import duckdb
import os
import pytest

# Get a fresh connection to DuckDB with the community extension binary loaded
@pytest.fixture
def duckdb_conn():
    extension_binary = os.getenv('HTTPSERVER_EXTENSION_BINARY_PATH')
    if (extension_binary == ''):
        raise Exception('Please make sure the `HTTPSERVER_EXTENSION_BINARY_PATH` is set to run the python tests')
    conn = duckdb.connect('', config={'allow_unsigned_extensions': 'true'})
    conn.execute(f"load '{extension_binary}'")
    return conn

def test_quack(duckdb_conn):
    duckdb_conn.execute("SELECT httpserve_start('0.0.0.0', 8123, '');");
    res = duckdb_conn.fetchall()
    assert(res[0][0] == "HTTP server started on 0.0.0.0:8123");

def test_quack(duckdb_conn):
    duckdb_conn.execute("SELECT * FROM read_json_auto('http://localhost:8123/?q=SELECT 1');");
    res = duckdb_conn.fetchall()
    assert(res[0][0] == "1");
