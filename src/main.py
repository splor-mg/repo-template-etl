from frictionless import Package

package = Package('datapackage.yaml')
resource = package.get_resource('consonants')
