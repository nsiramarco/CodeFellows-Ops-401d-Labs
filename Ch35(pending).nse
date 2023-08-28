description = [[
MySQL Privilege Checker
]]

portrule = function(host, port)
    return port.protocol == "tcp" and port.number == 3306
end

action = function(host, port)
    local creds = {}

    stdnse.print("Enter MySQL username: ")
    creds.username = io.read()

    stdnse.print("Enter MySQL password: ")
    creds.password = io.read("*l")

    local conn = mysql.connect{
        host = host.ip,
        port = port.number,
        username = creds.username,
        password = creds.password,
    }

    if not conn then
        stdnse.print_output("Failed to connect to MySQL server")
        return
    end

    local query = "SHOW GRANTS"
    local result, err = conn:query(query)

    if not result then
        stdnse.print_output("Failed to retrieve privileges: " .. err)
    else
        stdnse.print_output("Privileges for " .. creds.username .. "@" .. host.ip .. ":" .. port.number .. "\n" .. result[1][1])
    end

    conn:close()
end
