# Encodes a URL to a shortened URL.
#
# @param {string} longUrl
# @return {string}
require 'digest'
@base_tiny_url = "http://tinyurl.com/"
@dict_l2s = {}
@dict_s2l = {}
def encode(longUrl)
  if @dict_l2s[longUrl].nil?
    @dict_l2s[longUrl] = short_url = @base_tiny_url + Digest::SHA256.base64digest(longUrl)[0..5]
    @dict_s2l[short_url] = longUrl
    return short_url
  else
    return @dict_l2s[longUrl]
  end
end

# Decodes a shortened URL to its original URL.
#
# @param {string} shortUrl
# @return {string}
def decode(shortUrl)
  @dict_s2l[shortUrl]
end


# Your functions will be called as such:
# decode(encode(url))
