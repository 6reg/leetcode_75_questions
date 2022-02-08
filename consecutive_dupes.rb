def remove_dupes string
  string.split(" ").filter.with_index { |word, index| word != string.split(" ")[index + 1] }.join(" ")
end

puts remove_dupes "alpha beta beta gamma gamma alpha"
