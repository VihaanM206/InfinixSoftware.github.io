#include <SFML/Graphics.hpp>

int main() {
    // Create a window
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Game");

    // Create a rectangle shape
    sf::RectangleShape player(sf::Vector2f(50.f, 50.f));
    player.setFillColor(sf::Color::Green);
    player.setPosition(375.f, 275.f);  // Starting position

    // Set up the clock for smooth movement
    sf::Clock clock;

    while (window.isOpen()) {
        // Handle events
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        // Movement logic (simple player movement using arrow keys)
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
            player.move(-200.f * clock.getElapsedTime().asSeconds(), 0);
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
            player.move(200.f * clock.getElapsedTime().asSeconds(), 0);
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
            player.move(0, -200.f * clock.getElapsedTime().asSeconds());
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
            player.move(0, 200.f * clock.getElapsedTime().asSeconds());
        }

        // Clear the window
        window.clear();

        // Draw the player rectangle
        window.draw(player);

        // Display everything we just drew
        window.display();

        // Reset the clock for the next frame
        clock.restart();
    }

    return 0;
}
