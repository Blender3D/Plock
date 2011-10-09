# Maintainer: Blender3D <>

pkgname=plock
pkgver=1.0.2
pkgrel=1
pkgdesc="A clean and desktop-independent lockscreen."
arch=(i686 x86_64)
url="http://blender3d.github.com/Plock/"
license=('GPL')
depends=('python2' 'qt' 'python2-qt' 'python2-sip')
makedepends=('git')
conflicts=('xlock')

build() {
  cd "$srcdir"
  msg "Fetching latest release..."
  
  rm -Rf Plock/
  git clone git://github.com/Blender3D/Plock.git
}

package() {
  cd "$srcdir"
  
  mkdir $pkgdir/usr $pkgdir/usr/bin
  
  mv Plock/plock $pkgdir/usr/bin
  cd $pkgdir/usr/bin
  
  chmod +x plock
  
  ln -s plock xlock
}