# Maintainer: Blender3D <>

pkgname=plock
pkgver=1.0.0
pkgrel=1
pkgdesc="A clean desktop-independent lockscreen."
arch=(i686 x86_64)
url="http://blender3d.github.com/Plock/"
license=('GPL')
depends=('python2' 'qt' 'python2-qt' 'python2-sip')
makedepends=()
source=("https://github.com/Blender3D/Plock/tarball/master")
conflicts=('xlock')

build() {
  cd "$srcdir"
  msg "Downloading latest tarball..."
  
  wget --no-check-certificate $source -O plock-git.tar.gz
  msg "Finished download..."
}

package() {
  cd "$srcdir"
  tar -xf plock-git.tar.gz
  mkdir $pkgdir/usr $pkgdir/usr/bin
  
  mv xlock $pkgdir/usr/bin
  mv plock.py $pkgdir/usr/bin
    
  chmod +x $pkgdir/usr/bin/xlock
}