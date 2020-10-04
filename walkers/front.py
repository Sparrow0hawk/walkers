import imgui 
import glfw

from OpenGL.GL import *

class Front:

    def __init__(self, world, width, height):
        self.world = world 
        self.sim_active = False
        self.width = width
        self.height = height
        
        window = self.init_glfw()

        imgui.create_context()

        self.window = window

    def init_glfw(self):
        # Initialize the GLFW library
        if not glfw.init():
            return

        # OpenGL 3 or above is required
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        # OpenGL context should be forward-compatible
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)

        # Create a window in windowed mode and it's OpenGL context
        primary = glfw.get_primary_monitor()  # for GLFWmonitor
        window = glfw.create_window(
            self.width,  # width, is required here but overwritten by "glfw.set_window_size()" above
            self.height,  # height, is required here but overwritten by "glfw.set_window_size()" above
            "pyimgui-examples-glfw",  # window name, is overwritten by "glfw.set_window_title()" above
            None,  # GLFWmonitor: None = windowed mode, 'primary' to choose fullscreen (resolution needs to be adjusted)
            None  # GLFWwindow
        )

        # Exception handler if window wasn't created
        if not window:
            glfw.terminate()
            raise OSError("Could not initialize window")

        # Makes window current on the calling thread
        glfw.make_context_current(window)

        # Passing window to main()
        return window

    def update(self):

        if self.sim_active:
            self.update_sim()

        self.draw()

    def draw(self):
        return
        

    def update_sim(self):
        return
    
    def is_active(self):
        """Cycles a frame and returns whether the window remains open.

        Returns:
           True if the application is still open, otherwise False.
        """
        active = not glfw.window_should_close(self.window)

#        if active and not self.first:
#            imgui.pop_font()
#            imgui.render()
#            self.impl.render(imgui.get_draw_data())
#            glfw.swap_buffers(self.window)

#        if active:
#            glfw.poll_events()
#            self.impl.process_inputs()
#            imgui.new_frame()
#            imgui.push_font(self.font)
#            self.first = False

        return active