require 'json'

class MyHash
  N = 512
  MASK = (1 << N) - 1
  p = 0
  def initialize(p)
    @p = p
  end
  def create_table(p)
    #ps = CONFIG['p']
    #p = ps.inject(0) { |a, e| a | (1 << e) }
    Array.new(256) do |i|
      N.times do
        if (i >> (N - 1) & 1) == 1
          i = ((i << 1) ^ p) & MASK
        else
          i = (i << 1) & MASK
        end
      end
      puts i
      i
    end
  end

  def table
    @table ||= create_table(@p)
  end

  def hash(str, v = 0)
    hash = MASK ^ v
    str.unpack("C*").each do |v|
      hash = (table[((hash) >> (N - 8)) ^ v] ^ hash << 8) & MASK
    end
    hash ^ MASK
  end

  def hex_hash(str)
    "%0#{N / 4}x" % hash(str)
  end

  def str_hash(str)
    [hex_hash(str)].pack("H*")
  end
end
