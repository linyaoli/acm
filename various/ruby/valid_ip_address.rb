# @param {String} ip
# @return {String}
def valid_ip_address(ip)
  if (ip.include?'.') && count_split(ip, ".")
    items = ip.split(".")
    if items.size == 4
      items.each do |t|
        result = valid_ipv4(t)
        return "Neither" if result == false
      end
      return "IPv4"
    end
  elsif (ip.include?':') && count_split(ip, ":")
    items = ip.split(":")
    if items.size == 8
      items.each do |t|
        result = valid_ipv6(t)
        return "Neither" if result == false
      end
      return "IPv6"
    end
  end

  return "Neither"
end

def valid_ipv4(item)
  len = item.size
  if len > 0 && len < 4
    if item.to_i.to_s == item
      return false if item.to_i > 255
      return valid_char(item)
    end
  end

  return false
end

def valid_ipv6(item)
  len = item.size
  if len > 0 && len < 5
    return valid_char(item)
  end

  return false
end

def valid_char(item)
  item.each_char do |c|
    if (c =~ /[A-Fa-f0-9]/).nil?
      return false
    end
  end
  return true
end

def count_split(ip, splitter)
  len = ip.split(splitter).join().size
  if splitter == "."
    return true if ip.size - len == 3
  elsif splitter == ":"
    return true if ip.size - len == 7
  end
  return false
end

test_cases =[
  "172.16.254.1",
  "2001:0db8:85a3:0:0:8A2E:0370:7334",
  "256.256.256.256",
  "2001:0db8:85a3:0:0:8A2E:0370:7334:",
  "2001:0db8:85a3:00000:0:8A2E:0370:7334"
]

test_cases.each do |t|
  puts valid_ip_address(t)
end
