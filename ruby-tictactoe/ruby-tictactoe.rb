class TicTacToe
    def initialize
      @board = Array.new(3) { Array.new(3, ' ') }
      @current_player = 'X'
    end
  
    def play
      until game_over?
        display_board
        process_turn
        switch_players
      end
      display_board
      announce_result
    end
  
    private
  
    def display_board
      puts " #{@board[0].join(' | ')} "
      puts '---+---+---'
      puts " #{@board[1].join(' | ')} "
      puts '---+---+---'
      puts " #{@board[2].join(' | ')} "
    end
  
    def process_turn
      row, col = get_player_input
      @board[row][col] = @current_player
    end
  
    def get_player_input
      loop do
        print "Player #{@current_player}, enter your move (row,col): "
        input = gets.chomp.split(',').map(&:to_i)
        if valid_move?(input)
          return input
        else
          puts "Invalid move. Please enter row,col values between 0 and 2 that are not already taken."
        end
      end
    end
  
    def valid_move?(input)
      return false unless input.size == 2
      row, col = input
      return false unless (0..2).cover?(row) && (0..2).cover?(col)
      return @board[row][col] == ' '
    end
  
    def switch_players
      @current_player = @current_player == 'X' ? 'O' : 'X'
    end
  
    def game_over?
      win? || draw?
    end
  
    def win?
      lines = @board + @board.transpose + diagonals
      lines.any? { |line| line.uniq.size == 1 && line.first != ' ' }
    end
  
    def draw?
      @board.all? { |row| row.none?(' ') }
    end
  
    def diagonals
      [[@board[0][0], @board[1][1], @board[2][2]], [@board[0][2], @board[1][1], @board[2][0]]]
    end
  
    def announce_result
      if win?
        puts "Player #{@current_player} wins!"
      else
        puts "It's a draw!"
      end
    end
  end
  
  game = TicTacToe.new
  game.play