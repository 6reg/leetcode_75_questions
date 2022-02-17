def main

  def caesar_cipher(str, num)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_str = ""

    str.each_char do |char|
      old_idx = alphabet.index(char) #1?
      new_idx = old_idx + num
      new_char = alphabet[new_idx % 26]
      new_str += new_char
    end

    return new_str
  end

  puts caesar_cipher("apple", 1) #=> 'bqqmf"
  puts caesar_cipher("bootcamp", 2)
  puts caesar_cipher("zebra", 4)

end

if __FILE__ == $0
  main
end
