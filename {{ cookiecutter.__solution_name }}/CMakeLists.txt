# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimun_required (VERSION 3.8)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

project ("{{ cookiecutter.__solution_cmake_name }}")

{% if cookiecutter.same_dir %}
# Include sub-projects.
add_subdirectory ("{{ cookiecutter.__project_cmake_name }}")
{% else %}
# Add source to this project's executable.
add_executable (CMakeProject2 "{{ cookiecutter.__project_cmake_name }}.cpp" "{{ cookiecutter.__project_cmake_name }}.h")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET CMakeProject2 PROPERTY CXX_STANDARD 20)
endif()

# TODO: Add tests and install targets if needed.
{% endif %}
