using System;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;

class Program
{
    private DiscordSocketClient _client;

    static void Main(string[] args) => new Program().RunBotAsync().GetAwaiter().GetResult();

    public async Task RunBotAsync()
    {
        _client = new DiscordSocketClient();
        _client.Log += Log;

        await RegisterCommandsAsync();

        await _client.LoginAsync(TokenType.Bot, "your-bot-token");

        await _client.StartAsync();

        await Task.Delay(-1);
    }

    private Task Log(LogMessage arg)
    {
        Console.WriteLine(arg);
        return Task.CompletedTask;
    }

    public async Task RegisterCommandsAsync()
    {
        _client.MessageReceived += HandleCommandAsync;
    }

    private async Task HandleCommandAsync(SocketMessage arg)
    {
        var message = arg as SocketUserMessage;
        var context = new SocketCommandContext(_client, message);

        if (message.Author.IsBot) return;

        if (message.Content == "Ping")
        {
            await context.Channel.SendMessageAsync("Pong!");
        }
    }
}