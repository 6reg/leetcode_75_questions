#!/usr/bin/env ruby

class MegaGreeter
  attr_accessor :names

  def initialize ages = 10
    @names = names
    @ages = ages
  end

  def say_hi
    if @names.nil?
      puts "..."
    elsif @names.respond_to? "each"
      @names.each { |name| puts "Hello #{name}!" }
    else
      puts "Hello #{@names}!"
    end
  end

  def say_bye
    if @names.nil?
      puts "..."
    elsif @names.respond_to? "join"
      puts "Goodbye #{@names.join(", ")}. Come back Soon!"
    else
      puts "Goodbye #{names}."
    end
  end
end
  if __FILE__ == $0
    mg = MegaGreeter.new
    mg.say_hi
    mg.say_bye

    #Change name to "Zeke"
    mg.names = "Zeke"
    mg.say_hi
    mg.say_bye

    # Change to array
    mg.names = ["albert", "pujols", "jake"]
    mg.say_hi
    mg.say_bye

    # Change to nil
    mg.names = nil
    mg.say_hi
    mg.say_bye
  end
