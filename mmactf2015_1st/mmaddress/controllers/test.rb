require 'json'
require_relative 'session'
require_relative 'myhash'

#CONFIG = {'p' => ARGV.map{|x| x.to_i}}
CONFIG = {'pp' => ARGV[0].to_i}

json = '{"user":"gasol","password":"906c1d7272d2b854700af56b6fcccd38907ab12a09ac360efcf91b142cba2d9ff21b034f9a4f51ea68f7fbac3ba087e45b81ad6df9bf26d8563afa5367a4772a"}'
expect = 'tep3Eioz8XtQXNpteGHXeFtpi1ZzpZy4AVdxhmO+nw4NFM3/cF4P9JPyZpDgaxJeGUsS+++38BM1OpfcZnpGFQ=='
for p in (1..65535)
  h = MyHash.new(p)
  actual = [h.str_hash(json)].pack('m').split.join()
  puts actual
  puts expect
  if actual == expect
    puts p
    break
  end
end
__END__
cookie = 'eyJ1c2VyIjoiZ2Fzb2wiLCJwYXNzd29yZCI6IjkwNmMxZDcyNzJkMmI4NTQ3MDBhZjU2YjZmY2NjZDM4OTA3YWIxMmEwOWFjMzYwZWZjZjkxYjE0MmNiYTJkOWZmMjFiMDM0ZjlhNGY1MWVhNjhmN2ZiYWMzYmEwODdlNDViODFhZDZkZjliZjI2ZDg1NjNhZmE1MzY3YTQ3NzJhIn0=-----tep3Eioz8XtQXNpteGHXeFtpi1ZzpZy4AVdxhmO+nw4NFM3/cF4P9JPyZpDgaxJeGUsS+++38BM1OpfcZnpGFQ=='
s = Session.new(cookie)
__END__
