# CMakeList.txt : CMake project for CMakeProject1, include source and define
# project specific logic here.
#

# Add source to this project's executable.
add_executable ({{ cookiecutter.__project_name }} "{{ cookiecutter.__project_name }}.cpp" "{{ cookiecutter.__project_name }}.h")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET {{ cookiecutter.__project_name }} PROPERTY CXX_STANDARD 20)
endif()

# TODO: Add tests and install targets if needed.
