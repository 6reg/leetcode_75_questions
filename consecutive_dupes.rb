def del_consec_words string
  string.split(' ').filter.with_index { |word, index| word != string.split(' ')[index + 1] }.join(' ')   
end

puts del_consec_words 'alpha alpha beta beta gamma gamma gamma'
