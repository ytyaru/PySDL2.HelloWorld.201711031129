import sys, sdl2.ext

def run():
    RESOURCES = sdl2.ext.Resources(__file__, 'res')

    sdl2.ext.init()
    window = sdl2.ext.Window("こんにちは PySDL2 !!", size=(640, 480))
    window.show()

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(RESOURCES.get_path("star.png"))

    spriterenderer = factory.create_sprite_render_system(window)
    spriterenderer.render(sprite)

    processor = sdl2.ext.TestEventProcessor()
    processor.run(window)

    sdl2.ext.quit()

if __name__ == '__main__':
    print('sdl2 ver:', sdl2.__version__)
    print('sdl2 ver info:', sdl2.version_info)
    sys.exit(run())
