import org.javacord.api.DiscordApi;
import org.javacord.api.DiscordApiBuilder;

public class AnilistBot {

    public static void main(String[] args) {

        String token = args[0];

        DiscordApi anilistBot = new DiscordApiBuilder().setToken(token).login().join();

        anilistBot.addMessageCreateListener(msg -> {
            String message = msg.getMessageContent();
            if (message.charAt(0) == '.') {
                msg.getChannel().sendMessage("Hello World");
                System.out.println("Hello World");
            }
        });

    }

}
