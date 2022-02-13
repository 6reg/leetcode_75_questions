# This program takes a string as input and returns the string with any 
# duplicate words removed.

def main
  
  def remover string
    string.split(' ').filter.with_index { |word, index| word != string.split(' ')[index + 1] }.join(' ')
  end
  puts remover 'alpha alpha beta beta beta phi'
end


if __FILE__ == $0
  main
end
