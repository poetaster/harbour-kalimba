import QtQuick 2.0
import Sailfish.Silica 1.0

CoverBackground {
    Label {
        id: label
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 100
        text: qsTr("Kalimba")
    }
    Image {
        id: bg
        source: "../html/img/192.png"
        anchors.horizontalCenter: parent.horizontalCenter
        fillMode: Image.Pad
        anchors {
            margins: 10
            top: label.bottom
        }
    }


   /* CoverActionList {
        id: coverAction

        CoverAction {
            iconSource: "image://theme/icon-cover-next"
        }

        CoverAction {
            iconSource: "image://theme/icon-cover-pause"
        }
    }*/
}
