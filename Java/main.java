import discord4j.core.DiscordClient;
import discord4j.core.GatewayDiscordClient;
import discord4j.core.event.domain.message.MessageCreateEvent;

public class MyDiscordBot {
    public static void main(String[] args) {
        final String token = "MTE5OTQzMjI4NjQ0NjI5NzI4MA.GJ4u_h.ym92xAxydTb9tOLfzDm5fYAULGPTaPC62pOJyk"; 
        final DiscordClient client = DiscordClient.create(token);
        final GatewayDiscordClient gateway = client.login().block();

        gateway.on(MessageCreateEvent.class).subscribe(event -> {
            if (event.getMessage().getContent().equals("!ping")) {
                event.getMessage().getChannel().block().createMessage("Pong!").block();
            }
        });

        gateway.onDisconnect().block();
    }
}
